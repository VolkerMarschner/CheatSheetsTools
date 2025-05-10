# JavaScript & TypeScript Syntax Cheat Sheet

## Variables & Data Types

### JavaScript
```javascript
// Variable declarations
let x = 10;              // Block-scoped variable
const PI = 3.14;         // Constant (cannot be reassigned)
var name = "John";       // Function-scoped variable (avoid if possible)

// Primitive data types
let num = 42;            // Number
let str = "Hello";       // String
let bool = true;         // Boolean
let n = null;            // Null
let u = undefined;       // Undefined
let sym = Symbol("id");  // Symbol
let bigInt = 9007199254740991n; // BigInt

// Complex data types
let arr = [1, 2, 3];     // Array
let obj = {              // Object
  name: "John",
  age: 30
};
```

### TypeScript Additions
```typescript
// Type annotations
let age: number = 25;
let name: string = "Alice";
let isActive: boolean = true;
let anyValue: any = "anything";
let unknownValue: unknown = 42;

// Arrays
let numbers: number[] = [1, 2, 3];
let strings: Array<string> = ["a", "b", "c"];

// Tuples
let person: [string, number] = ["John", 25];

// Enums
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT"
}
let move: Direction = Direction.Up;

// Union types
let id: string | number = 101;

// Type aliases
type Point = {
  x: number;
  y: number;
};
let point: Point = { x: 10, y: 20 };

// Interfaces
interface User {
  name: string;
  age: number;
  readonly id: number;
  email?: string;  // Optional property
}
```

## Functions

### JavaScript
```javascript
// Function declaration
function add(a, b) {
  return a + b;
}

// Function expression
const subtract = function(a, b) {
  return a - b;
};

// Arrow function
const multiply = (a, b) => a * b;

// Default parameters
function greet(name = "Guest") {
  return `Hello, ${name}!`;
}

// Rest parameters
function sum(...numbers) {
  return numbers.reduce((total, num) => total + num, 0);
}

// Callback functions
function fetchData(callback) {
  // Simulate async operation
  setTimeout(() => {
    callback("Data received");
  }, 1000);
}
```

### TypeScript Additions
```typescript
// Function with type annotations
function add(a: number, b: number): number {
  return a + b;
}

// Optional parameters
function buildName(firstName: string, lastName?: string): string {
  return lastName ? `${firstName} ${lastName}` : firstName;
}

// Function overloading
function getItem(id: number): number;
function getItem(name: string): string;
function getItem(idOrName: number | string): number | string {
  return typeof idOrName === "number" ? idOrName * 2 : `Item ${idOrName}`;
}

// Generic functions
function identity<T>(arg: T): T {
  return arg;
}
```

## Control Flow

```javascript
// Conditionals
if (condition) {
  // code
} else if (anotherCondition) {
  // code
} else {
  // code
}

// Ternary operator
const result = condition ? "value if true" : "value if false";

// Switch statement
switch (expression) {
  case value1:
    // code
    break;
  case value2:
    // code
    break;
  default:
    // code
}

// Loops
for (let i = 0; i < 5; i++) {
  // code
}

for (const item of array) {
  // code
}

for (const key in object) {
  // code
}

while (condition) {
  // code
}

do {
  // code
} while (condition);

// Error handling
try {
  // code that might throw an error
} catch (error) {
  // handle error
} finally {
  // always executes
}
```

## Classes & Objects

### JavaScript
```javascript
// Object literal
const person = {
  name: "John",
  age: 30,
  greet() {
    return `Hello, my name is ${this.name}`;
  }
};

// Classes
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    return `Hello, my name is ${this.name}`;
  }

  static createAnonymous() {
    return new Person("Anonymous", 0);
  }
}

// Inheritance
class Employee extends Person {
  constructor(name, age, job) {
    super(name, age);
    this.job = job;
  }

  work() {
    return `${this.name} is working as a ${this.job}`;
  }
}
```

### TypeScript Additions
```typescript
// Classes with access modifiers
class Person {
  private id: number;
  protected age: number;
  public name: string;
  readonly birthDate: Date;

  constructor(name: string, age: number, birthDate: Date) {
    this.name = name;
    this.age = age;
    this.birthDate = birthDate;
    this.id = Math.random();
  }
}

// Implementing interfaces
interface Movable {
  move(distance: number): void;
  speed: number;
}

class Car implements Movable {
  speed: number = 0;
  
  move(distance: number): void {
    console.log(`Moving ${distance} miles`);
  }
}

// Abstract classes
abstract class Shape {
  abstract getArea(): number;
  
  display(): void {
    console.log(`Area: ${this.getArea()}`);
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }
  
  getArea(): number {
    return Math.PI * this.radius ** 2;
  }
}
```

## Modules

### JavaScript
```javascript
// Exporting
export const PI = 3.14;
export function square(x) {
  return x * x;
}
export default class Calculator {
  // class implementation
}

// Importing
import Calculator, { PI, square } from './math';
import * as math from './math';
```

### TypeScript Additions
```typescript
// Type exports
export interface Point {
  x: number;
  y: number;
}

export type Vector = [number, number, number];

// Import types
import type { Point, Vector } from './geometry';
```

## Asynchronous JavaScript

```javascript
// Promises
const promise = new Promise((resolve, reject) => {
  if (condition) {
    resolve('Success');
  } else {
    reject('Error');
  }
});

promise
  .then(result => console.log(result))
  .catch(error => console.error(error))
  .finally(() => console.log('Completed'));

// Async/await
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

// Promise methods
Promise.all([promise1, promise2])
  .then(results => console.log(results));

Promise.race([promise1, promise2])
  .then(result => console.log(result));

Promise.allSettled([promise1, promise2])
  .then(results => console.log(results));
```

## TypeScript Advanced Types

```typescript
// Intersection types
type Employee = Person & { employeeId: number };

// Type guards
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// Utility types
type Readonly<T> = { readonly [P in keyof T]: T[P] };
type Partial<T> = { [P in keyof T]?: T[P] };
type Pick<T, K extends keyof T> = { [P in K]: T[P] };
type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;

// Example usage
interface Todo {
  title: string;
  description: string;
  completed: boolean;
}

const todo: Readonly<Todo> = {
  title: "Learn TypeScript",
  description: "Study advanced types",
  completed: false
};

// Mapped types
type Nullable<T> = { [P in keyof T]: T[P] | null };

// Conditional types
type ExtractType<T> = T extends string ? "string" : "other";

// Template literal types
type EventName<T extends string> = `${T}Changed`;
type UserEvents = EventName<"name" | "email">;  // "nameChanged" | "emailChanged"
```

## ES6+ Features

```javascript
// Destructuring
const { name, age } = person;
const [first, second] = array;

// Spread operator
const newArray = [...array1, ...array2];
const newObj = { ...obj1, ...obj2 };

// Optional chaining
const value = obj?.prop?.field;

// Nullish coalescing
const result = value ?? defaultValue;

// Template literals
const message = `Hello, ${name}!`;

// Object property shorthand
const x = 10, y = 20;
const point = { x, y };

// Method shorthand
const obj = {
  sayHello() {
    console.log("Hello");
  }
};

// Computed property names
const propName = "dynamicProp";
const obj = {
  [propName]: 42
};
```
