import * as React from "react"
import Card from "@mui/material/Card"
import CardContent from "@mui/material/CardContent"
import Typography from "@mui/material/Typography"
import { Stat } from "./StatList"

export default function StatCard({ title, body }: Stat) {
  return (
    <Card sx={{ minWidth: 275, marginBottom: '5em' }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          {title}
        </Typography>

        <Typography variant="h5" component="div">
          {body}
        </Typography>
      </CardContent>
    </Card>
  )
}
