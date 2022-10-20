// # 9663. N-Queen

function findQueens(N) {
	// 이곳에 작성합니다.
    let chessboard = Array(N).fill(0)
    let answer = 0
    
    const check = (row) => {
        for (let i = 0; i < row; i++) {
            if ((chessboard[row] === chessboard[i]) || (Math.abs(chessboard[row]-chessboard[i]) === Math.abs(row-i))) {
                return false
            }
        }
        return true
    }
    
    const solve = (row) => {
        if (row >= N) {
            answer += 1    
        } else {
            for (let column = 0; column < N; column++) {
                chessboard[row] = column
                if (check(row)) {
                    solve(row+1)
                }
            }
        }
    }
    
    solve(0)
	return answer
}

console.log(findQueens(8)) // 92
