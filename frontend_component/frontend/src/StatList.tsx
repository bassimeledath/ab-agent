import * as React from "react"
import StatCard from "./StatCard"

export type Stat = {
  title: string
  body: number | string
}

type Prop = {
  stats: Stat[]
}

export default function StatList({ stats }: Prop) {
  return (
    <>
      {stats.map((stat) => (
        <StatCard {...stat} />
      ))}
    </>
  )
}
