export default class Currency {
  constructor(name, code) {
    this.name = '';
    this.code = '';
    this.name = name;
    this.code = code;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code === 'string') {
      this._code = code;
    } else {
      throw new Error('Code must be a string!');
    }
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('Name must be a string!');
    }
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
