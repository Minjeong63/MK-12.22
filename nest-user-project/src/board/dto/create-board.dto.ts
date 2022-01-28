import { IsString } from "class-validator";

export class CreateBoardDto {
    @IsString()
    readonly name: string;

    @IsString()
    readonly id: string;

    @IsString()
    readonly password: string;

    @IsString()
    readonly passwordCheck: string;
}