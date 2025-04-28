const object1 = {
    repository: undefined,
  };
  
  /* repository의 readme가 undefined인 경우 */
  const object2 = {
    repository: {
      readme: undefined,
    },
  };
  
  /** repository.readme 모두가 존재하는 경우 */
  const object3 = {
    repository: {
      readme: {
        extension: 'md',
        content: '금융을 쉽고 간편하게',
      }
    }
  };

  function safelyGet(obj, pathStr) {
    const path = pathStr.split(".");
    let answer = obj

    for (const str of path) {
      answer = answer[str];

      if (answer === undefined) {
        return answer;
      }
    }

    return answer;
  }

  
  console.log(safelyGet(object1, 'repository.readme.extension'));
  // // -> 반환 값: undefined
  
  console.log(safelyGet(object1, 'repository.readme'))
  // -> 반환 값: undefined
  
  console.log(safelyGet(object1, 'repository'))
  // -> 반환 값: undefined
  
  console.log(safelyGet(object2, 'repository.readme.extension'))
  // -> 반환 값: undefined
  
  console.log(safelyGet(object2, 'repository.readme'))
  // -> 반환 값: undefined
  
  console.log(safelyGet(object2, 'repository'))
  // -> 반환 값: { readme: undefined }
  
  console.log(safelyGet(object3, 'repository.readme.extension'))
  // -> 반환 값: 'md'
  
  console.log(safelyGet(object3, 'repository.readme'))
  // -> 반환 값: { extension: 'md' }