from enum import Enum


class ProductData:
    products = [
        {
            "id": "013ebceb3e174b3aaa00aee3ef5c46bb",
            "name": "Perfume",
            "description": "Perfumes can be defined as substances that emit and diffuse a pleasant and fragrant odor. They consist of manmade mixtures of aromatic chemicals and essential oils. Until the nineteenth century perfumes were usually composed of natural aromatic oils.",
            "price": "400",
            "color": "Pink",
            "slug": "perfume",
            "image": "image/upload/v1661307313/products/perfume_dxah4o.jpg",
            "category_id": "5",
        },
        {
            "id": "0f7d30b8d012412b98911716ad9639e2",
            "name": "Leather jacket",
            "description": "Leather has a number of very special, natural properties: It is breathable, heat-insulating, stretchy, tearproof and abrasion-resistant and acts a barrier against moisture evaporation. It is also robust, making the shoe more stable and functional. From a stylistic point of view, it gives the shoe its very unique look.",
            "price": "80",
            "color": "Brown",
            "slug": "leather-jacket",
            "image": "image/upload/v1661307312/products/d65dafc07638c71e20220ade57604e9a_c98d7e.jpg",
            "category_id": "1",
        },
        {
            "id": "21f77c6d90654e5ea6fc5efd83eb48ac",
            "name": "Bowl",
            "description": "A bowl typically is a round dish or container generally used for preparing, serving, or consuming food. The interior of a bowl is characteristically shaped like a spherical cap, with the edges and the bottom forming a seamless curve. This makes bowls especially suited for holding liquids and loose food, as the contents of the bowl are naturally concentrated in its center by the force of gravity. The exterior of a bowl is most often round but can be of any shape, including rectangular.",
            "price": "20",
            "color": "White",
            "slug": "bowl",
            "image": "image/upload/v1661307312/products/bowl2_zglidk.jpg",
            "category_id": "6",
        },
        {
            "id": "4f41959836ed4d88b0ca5cf949ea3e03",
            "name": "Wrist watch",
            "description": "A small watch that is attached to a bracelet or strap and is worn around the wrist.",
            "price": "100",
            "color": "Gold",
            "slug": "wrist-watch",
            "image": "image/upload/v1661307314/products/wristclock_tfyby6.webp",
            "category_id": "3",
        },
        {
            "id": "76e4dc0cb1ba45b288de53016f22a124",
            "name": "Backpack",
            "description": "A large pack (as of canvas or nylon) that is supported by an external or internal frame (as of aluminum) and is used especially for carrying supplies when hiking and camping",
            "price": "100",
            "color": "Gray",
            "slug": "backpack",
            "image": "image/upload/v1661307311/products/backbag3_dkunrz.jpg",
            "category_id": "4",
        },
        {
            "id": "7deca236585c4254ad6d474d51f93956",
            "name": "Leather shoes",
            "description": "Leather has a number of very special, natural properties: It is breathable, heat-insulating, stretchy, tearproof and abrasion-resistant and acts a barrier against moisture evaporation. It is also robust, making the shoe more stable and functional. From a stylistic point of view, it gives the shoe its very unique look.",
            "price": "200",
            "color": "Brown",
            "slug": "leather-shoes",
            "image": "image/upload/v1661307313/products/shoes_oopaq9.webp",
            "category_id": "2",
        },

    ]


class CategoryData:
    categories = [
        {
            "id": "1",
            "name": "Clothes",
            "slug": "clothes",
        },
        {
            "id": "2",
            "name": "Footwear",
            "slug": "footwear",
        },
        {
            "id": "3",
            "name": "Jewelry",
            "slug": "jewelry",
        },
        {
            "id": "4",
            "name": "Backpack",
            "slug": "backpack",
        },
        {
            "id": "5",
            "name": "Perfume",
            "slug": "perfume",
        },
        {
            "id": "6",
            "name": "Utensil",
            "slug": "utensil",
        },
    ]
