import { Injectable } from '@nestjs/common';
import { Board } from './board.entity';
import { CreateBoardDto } from './dto/create-board.dto';

@Injectable()
export class BoardService {
    private board: Board[] = [];

    getAll() {
        return "게시판 내용 모두 가져오기"
    }

    create(boardData: CreateBoardDto) {
        this.board.push({
            key: this.board.length + 1,
            ...boardData
        });
    }
}
