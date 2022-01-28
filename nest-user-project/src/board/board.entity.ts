import { BaseEntity, Column, Entity, PrimaryGeneratedColumn } from "typeorm";

@Entity()
export class Board extends BaseEntity {
    @PrimaryGeneratedColumn()
    key: number;

    @Column()
    id: string;

    @Column()
    name: string;

    @Column()
    password: string;

    @Column()
    passwordCheck: string;
}
