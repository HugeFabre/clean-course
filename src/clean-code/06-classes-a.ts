( () => {

    type Gender = 'M' | 'F';

    class Person{
        constructor(
            public name : string,
            public gerden : Gender,
            public birthdate : Date){
        }
    }

    class User extends Person{
        constructor(
            public email: string,
            public role : string,
            public lastAccess : Date
        ){
                
        }
    }

})(); 