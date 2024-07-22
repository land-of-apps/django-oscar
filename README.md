# How to use this repo

This project is an ideal Python Django project to use with the [AppMap Navie](https://appmap.io/navie/) AI Architect.

You can use this project to ask various questions of AppMap Navie using the `@diagram` command prefix.  
This will generate Mermaid diagrams that you can use within GitHub Issues & Pull Requests, or otherwise share 
with members of your team. 


## Example Diagrams

### Example Question (Sequence Diagram)
```
@diagram the functional steps involved when a new user registers for the service.
```

```mermaid
sequenceDiagram
    participant User as User
    participant RegistrationForm as "Registration Form"
    participant RegisterUserMixin as "Register User Mixin"
    participant UserModel as "User Model"
    participant EmailService as "Email Service"

    User->>RegistrationForm: Fills registration form
    RegistrationForm->>RegisterUserMixin: Submits form data
    activate RegisterUserMixin
    
    RegisterUserMixin->>UserModel: Save user instance
    activate UserModel
    UserModel-->>RegisterUserMixin: Returns user object
    deactivate UserModel
    
    RegisterUserMixin->>EmailService: Send registration email
    activate EmailService
    EmailService-->>RegisterUserMixin: Confirmation
    deactivate EmailService
    
    RegisterUserMixin-->>RegistrationForm: Returns user object
    deactivate RegisterUserMixin

    RegistrationForm-->>User: Shows success message
```

![Navie Sequence Diagram Image](navie-sequence-diagram-example.png)


### Example Question (Entity Relationship)

```
@diagram the entity relationships between products and other important data objects.  
```


```mermaid
erDiagram
  PRODUCT {
    int id
    string title
    string upc
    text description
  }
  
  PRODUCTCLASS {
    int id
    string name
    string slug
  }
  
  PRODUCTATTRIBUTE {
    int id
    string name
    string code
    string required
    string type
  }
  
  PRODUCTCATEGORY {
    int id
    int product_id
    int category_id
  }
  
  CATEGORY {
    int id
    string name
    string slug
  }
  
  PRODUCTIMAGE {
    int id
    string original
    string caption
    int product_id
  }

  PRODUCTRECOMMENDATION {
    int id
    int primary_id
    int recommendation_id
  }
  
  PRODUCT ||--o{ PRODUCTCLASS : "belongs to"
  PRODUCT ||--o{ PRODUCTATTRIBUTE : "has"
  PRODUCT ||--o{ PRODUCTCATEGORY : "belongs to"
  PRODUCT ||--o{ PRODUCTIMAGE : "has"
  PRODUCT ||--o{ PRODUCTRECOMMENDATION : "has"

  CATEGORY ||--o{ PRODUCTCATEGORY : "includes"
```

![Navie Entitiy Relationship](navie-entity-relationship-example.png)

### Example Question (Flow Chart)

```
@diagram using a flow chart how product sales tax is calculated
```

```mermaid
flowchart TD
    A["Basket"] --> B["BaseCharge.calculate"]
    B --> C{"Has Discount?"}
    C -->|No| D["Calculate excl_tax and incl_tax from BaseCharge"]
    C -->|Yes| E["Apply Discount: Offer.shipping_discount"]
    E --> F["Calculate excl_tax and incl_tax after discount"]
    D --> G["Check if incl_tax is 0"]
    F --> G
    G -->|Yes| H["Return zero excl_tax"]
    G -->|No| I["Calculate excl_tax proportionally"]
    I --> J["Return prices.Price object with updated excl_tax and incl_tax"]
    H --> J
```
![Navie Flow Chart](navie-flow-chart.png)