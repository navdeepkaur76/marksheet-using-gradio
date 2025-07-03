import gradio as gr
def calculate_marks(name,rollno,math,science,english):
    try:
        math=int(math)
        science=int(science)
        english=int(english)
    except ValueError:
        return "invalid marks","",""
    total=math+science+english
    percentage=round((total/300)*100,2)
    return  f"{name}",f"{rollno}",f"{total}",f"{percentage}%"
with gr.Blocks()as demo:
    gr.Markdown("##Student Marksheet")
    with gr.Row():
        name=gr.Textbox(label="Name")
        rollno=gr.Textbox(label="Roll Number")
    with gr.Row():
        math=gr.Textbox(label="Math Marks(out of 100)")
        science=gr.Textbox(label="Science Marks(out of 100)")
        english=gr.Textbox(label="English Marks(out of 100)")
        submit_btn=gr.Button("Calculate total & percentage")
    with gr.Row():
        output_name=gr.Textbox(label="student Name")
        output_roll=gr.Textbox(label="Roll Number")
    with gr.Row():
        total=gr.Textbox(label="Total marks(out of 300)")
        percent=gr.Textbox(label="Percentage")
    submit_btn.click(
        calculate_marks,
        inputs=[name,rollno,math,science,english],
        outputs=[output_name,output_roll,total,percent]
        )
    demo.launch()
    
