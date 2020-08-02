myinput = raw_input('Action : ')

request_type = raw_input("Type of Request : ")


print('CONSTANSTS\n-----------')
constants = """
export const {0}_FAIL= '{0}_FAIL'
export const {0}_SUCCESS= '{0}_SUCCESS'
export const {0}_START= '{0}_START'
""" .format(str(myinput))    
print(constants)

print('REDUCERS\n-----------')

reducers = """
if (action.type=== {0}_START) return{{ ...state,loading:true}}
if (action.type=== {0}_FAIL) return {{ ...state,loading:false,error_message:action.error_message}}
if (action.type=== {0}_SUCCESS){{
}}
""".format(myinput)

print(reducers)

print('ACTIONS\n-----------')

actions= """
export const {1}_success =(payload)=>({{type: {0}_SUCCESS,payload}})
export const {1}_start=()=>({{type:{0}_START}})
export const {1}_fail=(error_message)=>({{type:{0}_FAIL,error_message}})
}}
""".format(myinput,myinput.lower())

print(actions)

print('TYPE OF REQUEST \n --------')

request = """
 export const {action}_async=(body,callback)=>{{
    return (dispatch)=>{{
      dispatch({action}_start())
      axios
      .{request_type}.(`{{URL}}admin/carriers`,body)
      .then((response)=> {{
        dispatch({action}_success(response.data.carrier));
        console.log(response);
        api_callback(true,'Success','Success')
        callback(true)
      }})
      .catch(function(error) {{
        if (error.response) {{
           dispatch({action}_fail(error.response.data.error_message))
           callback(false)
           api_callback(false,'Fail','Fail Occured')
           console.log(error.response.data);
           console.log(error.response.status);
           console.log(error.response.headers);
           console.log("Error", error.message);
           console.log("error 1");
        }} else if (error.request) {{
          console.log(error.request);
        }} else {{
          console.log("Error", error.message);
        }}
           console.log(error.config);
        }});
        }};;
      }}
""".format(request_type=request_type.lower(),url='http://woocargo.com/api/',action=myinput.lower())
print(request)
