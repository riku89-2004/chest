//小分類のデータ
const subCategoryData = {
    fruits: [
      { value: "apple", text: "りんご" },
      { value: "banana", text: "バナナ" },
      { value: "orange", text: "オレンジ" }
    ],
    vegetables: [
      { value: "carrot", text: "にんじん" },
      { value: "potato", text: "じゃがいも" },
      { value: "cabbage", text: "キャベツ" }
    ],
    animals: [
      { value: "cat", text: "猫" },
      { value: "dog", text: "犬" },
      { value: "bird", text: "鳥" }
    ]
  };

//大分類と小分類の要素を取得
const mainCategory = document.getElementById("main-category");
const subCategory = document.getElementById("sub-category");

//大分類が変更されたときの処理
mainCategory.addEventListener("change", () => {
    const selectedCategory = mainCategory.value;

    //小分類の選択肢をリセット
    subCategory.innerHTML = `<option value="">--${selectedCategory ? '選択してください' : '大分類を選択してください'}--</option>`;
  
    //小分類の選択肢を追加
    if (selectedCategory && subCategoryData[selectedCategory]) {
        subCategoryData[selectedCategory].forEach(item => {
            const option = document.createElement("option");
            option.value = item.value;
            option.textContent = item.text;
            subCategory.appendChild(option);
        });
    }
});
