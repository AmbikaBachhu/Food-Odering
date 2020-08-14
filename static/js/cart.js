var updatebtns = document.getElementsByClassName('update-cart');

for (i=0;i<updatebtns.length;i++){
   updatebtns[i].addEventListener('click',function () {
        var foodId = this.dataset.food;
        var action = this.dataset.action;
       console.log('foodId:',foodId,'Action:',action);
       console.log('User:',user);
       if (user == 'AnonymousUser') {
       	   addCookieItem(foodId,action)
  } else {
           updateUserOrder(foodId,action)
  }

   })
}
function updateUserOrder(foodId, action){
	console.log('User is authenticated, sending data...');
    var csrftoken = getToken('csrftoken');
		var url = '/update_item/';

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'foodId':foodId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}




function addCookieItem(foodId, action){
	console.log('User is not authenticated')

	if (action === 'add'){
		if ( carts[foodId]===undefined){
		carts[foodId] = {'quantity':1}

		}else{
			carts[foodId]['quantity'] += 1
		}
	}

	if (action === 'remove'){
		carts[foodId]['quantity'] -= 1

		if (carts[foodId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete carts[foodId];
		}
	}
	console.log('CART:', carts);
	document.cookie ='cart=' + JSON.stringify(carts) + ";domain=;path=/"

	location.reload()
}

