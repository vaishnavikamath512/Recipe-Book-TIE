function addRecipe() {
  var recipeNameInput = document.getElementById('recipeName');
  var ingredientsInput = document.getElementById('ingredients');
  var instructionsInput = document.getElementById('instructions');
  var recipeList = document.getElementById('recipeList');

  if (
    recipeNameInput.value.trim() === '' ||
    ingredientsInput.value.trim() === '' ||
    instructionsInput.value.trim() === ''
  ) {
    alert('Please fill in all fields.');
    return;
  }

  var recipeDiv = document.createElement('div');
  recipeDiv.className = 'recipe';

  var recipeHeader = document.createElement('h2');
  recipeHeader.textContent = recipeNameInput.value;

  var ingredientsPara = document.createElement('p');
  ingredientsPara.textContent = 'Ingredients: ' + ingredientsInput.value;

  var instructionsPara = document.createElement('p');
  instructionsPara.textContent = 'Instructions: ' + instructionsInput.value;

  recipeDiv.appendChild(recipeHeader);
  recipeDiv.appendChild(ingredientsPara);
  recipeDiv.appendChild(instructionsPara);

  recipeList.appendChild(recipeDiv);

  // Clear input fields
  recipeNameInput.value = '';
  ingredientsInput.value = '';
  instructionsInput.value = '';
}
