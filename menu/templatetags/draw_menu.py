from django import template

from menu.models import MenuItem

register = template.Library()

def get_children(self): # add to model class?
    childs = []
    for node in self.__class__.all_items:
        if (node.level == self.level + 1 and node.lft > self.lft
        and node.rht < self.rht):
            childs.append(node)

    return childs

setattr(MenuItem, 'get_children', get_children)


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, slug):  # takes slug as argument
    all_items = MenuItem.objects.select_related('menu').filter(menu__slug=slug)
    last = context.request.get_full_path()

    # Find target.
    target = False
    for item in all_items:
        if item.get_url() == last:
            
            target = item
            break
    # If target not exist stick to root element.
    if not target:
        target = all_items[0] 

    root_list = [all_items[0]]
    if target.level >= 1:
        # find ancestor in lvl=1. It's gonna be the last item in the list.
        lookup = [item for item in all_items if item.lft <= target.rht 
                    and item.level == 1]
        # ancestor must be last item in lookup as items ordered by lft keys.
        ancestor = lookup[-1]
        # add all items in lvl=1.
        root_list += [item for item in all_items if item.level == 1]
        lvl = 2
        while lvl <= target.level:
            # List items between ancestor and target per level of iteration.
            addition = [item for item in all_items if item.lft > ancestor.lft 
                            and item.lft < ancestor.rht and item.level == lvl]
            lookup = [item for item in all_items if item.lft <= target.rht 
                        and item.level == lvl]
            ancestor = lookup[-1]
            # Include the addition in root_list.
            root_list += addition
            lvl += 1
    # Add direct children of target.
    children = [item for item in all_items if item.lft > target.lft 
                    and item.rht < target.rht and item.level == target.level + 1]
    root_list += children

    MenuItem.all_items = root_list

    return { 'node_list': [root_list[0]], 'context': context }
