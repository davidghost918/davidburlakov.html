document.addEventListener('DOMContentLoaded', () => {
    const menuItems = document.querySelectorAll('.menu-item > span');

    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            const parentItem = item.parentElement;
            const subMenu = parentItem.querySelector('.sub-menu');

            if (subMenu) {
                if (parentItem.classList.contains('active')) {
                    parentItem.classList.remove('active');
                } else {
                    parentItem.classList.add('active');
                }
            } else {
                alert('Вы можете пройти по этой ссылке.');
            }
        });
    });
});
