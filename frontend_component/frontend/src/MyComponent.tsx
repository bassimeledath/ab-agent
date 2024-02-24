import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import StatList from "./StatList"
import { Grid } from "@mui/material"

interface State {
  numClicks: number
  isFocused: boolean
}
type Props = {
  name: string[]
  key: string[]
}

class MyComponent extends StreamlitComponentBase<State, Props> {
  public state = { numClicks: 0, isFocused: false }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    const names = this.props.args["name"]
    const keys = this.props.args["key"]
    const stats = names.map((title, i) => ({
      title: keys[i],
      body: title,
    }));

    return (
      <Grid container spacing={2}>
        <StatList stats={stats} />
      </Grid>
    )
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(MyComponent)
