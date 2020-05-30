import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Background from './human_factors.png';
import 'bootstrap/dist/css/bootstrap.min.css';

//loads in the background picture (human factors thing)
var bground = {
    backgroundImage: `url(${Background})`,
    width: "100%",
    height: "8000px",
    backgroundAttachment: "scroll",
  };
  
  //sets the background image to the "human factors" theme image
  class BACKGROUND_IMAGE extends React.Component {
    render() {
      return(
        <div style={bground}>
        </div>
      );
    }
  }

  
ReactDOM.render(
  <div>
  <BACKGROUND_IMAGE />    
  </div>,
  document.getElementById('root')
);

//IGNORE THE REST BELOW

  // //import L from 'leaflet';

// import 'leaflet/dist/leaflet.css';
// import styled from 'styled-components';
// //import {ComposableMap, Geographies, Geography} from "react-simple-maps";

//make a wrapper for the map to render
// const Wrapper = styled.div`
//     width: ${props => props.width};
//     height: ${props => props.height};
// `;

// //creates an example map of the US with a sick dark theme
// export default class SimpleExample extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       lat: 42.2808,
//       long: -83.7430, 
//       zoom: 10,
//     };
//   }

//   componentDidMount() {
//     this.map = L.map(`map`, {
//       center: [this.state.lat, this.state.long],
//       zoom: this.state.zoom
//     });

//     L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
//         maxZoom: 20,
//       }).addTo(this.map);
//   }

//   render() {
//     return <Wrapper width='1200px' height='700px' id='map' />;
//   }
// }

  //this creates a basic world map using react-simple-maps: a viable option but not what we
  //are likely going to use
  // const geoURL = "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";
  // //creates a very simple map of the US by county
  // class USAmap extends React.Component {
  //   render() {
  //     return(
  //       <div>
  //         <ComposableMap>
  //           <Geographies geography={geoURL}>
  //             {({geographies}) =>
  //               geographies.map(geography => <Geography key = {geography.rsmKey} geography = {geography} />
  //             )}
  //           </Geographies>
  //         </ComposableMap>
  //       </div>
  //     );
  //   }
  // }
  
  // //this can render all of the classes in a row
  // class WrapperComponent extends React.Component {
  //   render() {
  //     return(
        
  //     );
  //   }
  // }
