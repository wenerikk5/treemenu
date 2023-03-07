from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Menu, MenuItem


admin.site.register(Menu)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # Add button to update all keys and levels.
    change_list_template = 'entities/menuitem_changelist.html'
    list_display = ['name', 'parent', 'menu']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('UpdateKeys/', self.update_tree),
        ]
        return my_urls + urls

    def update_tree(self, request):
        def update_menu(slug):
            all_items = MenuItem.objects \
                .select_related('menu') \
                .filter(menu__slug=slug) \
                .order_by('id')

            def get_children(target):
                print('target:', target)
                result = []
                for item in all_items:
                    print('item:', item)
                    if item.name == all_items[0].name:
                        print('=====ROOT ITEM:', item)
                        continue
                    if item.parent.name == target.name:
                        result.append(item)
                return result

            def rebuild_tree(parent, left, lvl):
                # update left and right keys
                right = left + 1

                result = get_children(parent)
                for child in result:
                    right = rebuild_tree(child, right, lvl + 1)
                
                parent.lft = left
                parent.rht = right
                parent.level = lvl
                parent.save()

                return right + 1
                
            rebuild_tree(all_items[0], 1, 0)

        for menu in Menu.objects.all():
            update_menu(menu.slug)

        self.message_user(request, "Ключи и уровни всех меню обновлены!")
        return HttpResponseRedirect("../")
