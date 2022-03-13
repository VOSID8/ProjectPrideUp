const createNav = () => {
    let nav = document.querySelector('.navbar');

    nav.innerHTML = `
    <div class="nav">
    <img src="static/shop/images/logo.png" class="brand-logo" alt="">
    <div class="nav-items">
        <div class="search">
            <input type="text" class="search-box" placeholder="search brand, product">
            <button class="search-btn">search</button>
        </div>
        <a href="#"><img src="static/shop/images/user.png" alt=""></a>
        <a href="#"><img src="static/shop/images/cart.png" alt=""></a>
    </div>
        </div>
    <ul class="links-container">
    <li class="link-item"><a href="#" class="link">Home</a></li>
    <li class="link-item"><a href="#" class="link">Ally</a></li>
    <li class="link-item"><a href="#" class="link">Merch</a></li>
    <li class="link-item"><a href="#" class="link">Homemade</a></li>

    </ul>
    `;
}

createNav();