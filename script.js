//小分類のデータ
const subCategoryData = {
    OTEith: [
      { value: "abekenta", text: "阿部憲太" },
      { value: "iimure", text: "飯牟礼" },
      { value: "iwai", text: "岩井" }
    ],
    OTSeth: [
      { value: "inokuma", text: "猪熊" },
      { value: "iwamoto", text: "岩本" },
      { value: "kasahara", text: "笠原" }
    ],
    OTSith: [
      { value: "asami", text: "浅見" },
      { value: "abeyuuki", text: "阿部優貴" },
      { value: "itimura", text: "市村" }
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
