<template>
    <div class="con">
        <h2 class="name">
        {{ monthName }} 
        </h2>
        
        <table class="sp">
            <tr>
                <th v-for="weekName in weekShortNames">
                    <div class="table-header">
                        {{ weekName }}
                    </div>
                </th>
            </tr>
            <tr v-for="week in weeksCount" class="day-between">
                <th v-for="day in 7" >

                    <div class="day-number">
                        {{ day + (7 * (week - 1))  }} 
                    </div>
                    <GridDay
                        :schedule="schedule[week-1][day - 1]"
                    />
                </th>
            </tr>
        </table>
    </div>
</template>

<script>
import GridDay from '@/components/GridDay.vue'
export default {
    data() {
        return {
            monthName: "Апрель",
            weeksCount: Math.round(30 / 7),
            weekShortNames: ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'],
            schedule: [
                [
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '10:00',
                            time2: '14:00'
                        },
                        {
                            name: 'Философия',
                            time1: '12:00',
                            time2: '13:00'
                        }
                    ],
                    [
                        {
                            name: 'Правоведение',
                            time1: '15:00',
                            time2: '16:00'
                        },
                        {
                            name: 'Материаловдение',
                            time1: '17:00',
                            time2: '18:00'
                        }   
                    ],
                    [
                        {
                            name: 'Практика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Философия',
                            time1: '12:00',
                            time2: '13:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '14:00',
                            time2: '15:00'
                        },
                        {
                            name: 'Философия',
                            time1: '16:00',
                            time2: '17:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '18:00',
                            time2: '19:00'
                        },
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '13:00',
                            time2: '14:00'
                        },
                        {
                            name: 'Философия',
                            time1: '16:00',
                            time2: '17:00'
                        }
                    ],
                    [
                        {
                            name: 'Философия',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Философия',
                            time1: '10:00',
                            time2: '11:00'
                        },
                    ]
                ],
                [
                    [
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Правоведение',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Правоведение',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Практика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Статистика',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Статистика',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Философия',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        },
                    ]
                ],
                [
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '10:00',
                            time2: '14:00'
                        },
                        {
                            name: 'Философия',
                            time1: '12:00',
                            time2: '13:00'
                        }
                    ],
                    [
                        {
                            name: 'Правоведение',
                            time1: '15:00',
                            time2: '16:00'
                        },
                        {
                            name: 'Материаловдение',
                            time1: '17:00',
                            time2: '18:00'
                        }
                    ],
                    [
                        {
                            name: 'Практика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Философия',
                            time1: '12:00',
                            time2: '13:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '14:00',
                            time2: '15:00'
                        },
                        {
                            name: 'Философия',
                            time1: '16:00',
                            time2: '17:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '18:00',
                            time2: '19:00'
                        },
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '13:00',
                            time2: '14:00'
                        },
                        {
                            name: 'Философия',
                            time1: '16:00',
                            time2: '17:00'
                        }
                    ],
                    [
                        {
                            name: 'Философия',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Философия',
                            time1: '10:00',
                            time2: '11:00'
                        },
                    ]
                ],
                [
                    [
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Правоведение',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Правоведение',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Практика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Статистика',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Статистика',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Теоретическая мехника',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'Высшая математика',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'Философия',
                            time1: '10:00',
                            time2: '11:00'
                        }
                    ],
                    [
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        },
                        {
                            name: 'История',
                            time1: '10:00',
                            time2: '11:00'
                        },
                    ]
                ],

            ]
        }
    },
    components: {
        GridDay
    }
}
</script>

<style>

table {
    width: 100%;
    border-collapse: collapse;
}

.con {
    margin-top: 1rem;
    padding-bottom: 2rem;
}

.table-header {
    margin-top: .5rem;
    background-color: rgb(203, 203, 203);
}

.name {
    text-align: center;
}

.day-number {
    text-align: right;
    color: rgba(0, 0, 0, 0.434);
}
tr {

}
</style>