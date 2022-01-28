import { Body, Controller, Get, Post } from '@nestjs/common';
import { BoardService } from './board.service';
import { CreateBoardDto } from './dto/create-board.dto';

@Controller('board')
export class BoardController {
    constructor(private boardService: BoardService) { }


    @Get()
    getAll() {
        return this.boardService.getAll()
    }

    @Post()
    create(@Body() createBoardDto: CreateBoardDto) {
        return this.boardService.create(createBoardDto);
    }
}
