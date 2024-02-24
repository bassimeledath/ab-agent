import * as React from "react"
import StatCard from "./StatCard"
import { Grid } from "@mui/material"

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
        <Grid item sm={12} lg={6} md={6} xs={12}>
          <StatCard {...stat} />
        </Grid>
      ))}
    </>
  )
}
