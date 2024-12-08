function Signup() {
  return (
    <div className="modal md">
      <div style={{marginBottom:"16px"}}>
        <h2>Sign Up</h2>
      </div>
      <div className="signup-form">
        <div className="input">
          <label className="required">Name</label>
          <input className="" type="text" placeholder="Name"/>
        </div>
        <div className="input">
          <label className="required">Email</label>
          <input type="text"  placeholder="Email" />
        </div>
        <div className="input">
          <label className="required">Password</label>
          <input type="text" className="required" placeholder="Password" />
        </div>
        <div className="input">
          <label className="required">Confirm Password</label>
          <input type="text" className="fullwidth" placeholder="Password"/>
        </div>
        <div>
          <p>Already have account? Login</p>
        </div>
        <div style={{alignSelf:"center"}}>
          <button className="btn-primary">Register</button>
        </div>
      </div>
    </div>
  );
}

export default Signup;
