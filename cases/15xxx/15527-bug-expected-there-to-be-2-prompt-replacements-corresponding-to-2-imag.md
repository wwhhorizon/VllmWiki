# vllm-project/vllm#15527: [Bug]: Expected there to be 2 prompt replacements corresponding to 2 image items, but instead found 0 prompt replacements!

| 字段 | 值 |
| --- | --- |
| Issue | [#15527](https://github.com/vllm-project/vllm/issues/15527) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Expected there to be 2 prompt replacements corresponding to 2 image items, but instead found 0 prompt replacements!

### Issue 正文摘录

### Your current environment ```this is my code llm = LLM( model="/home/....../environment/internvl2_5/InternVL2_5-4B-MPO", trust_remote_code=True, # Required to load Phi-3.5-vision max_model_len=4096, # Otherwise, it may not fit in smaller GPUs limit_mm_per_prompt={"image": 2}, # The maximum number to accept ) # Refer to the HuggingFace repo for the correct format to use prompt = " \n \n \nWhat is the content of each image? \n \n" # Load the images using PIL.Image image1 = Image.open("/home/......//environment/internvl2_5/InternVL2_5-26B-MPO/examples/1.jpg") image2 = Image.open("/home/......//environment/internvl2_5/InternVL2_5-26B-MPO/examples/2.jpg") outputs = llm.generate({ "prompt": prompt, "multi_modal_data": { "image": [image1, image2] }, }) for o in outputs: generated_text = o.outputs[0].text print(generated_text) ``` ### 🐛 Describe the bug RuntimeError: Expected there to be 2 prompt replacements corresponding to 2 image items, but instead found 0 prompt replacements! Either the prompt text has missing/incorrect tokens for multi-modal inputs, or there is a problem with your implementation of merged multi-modal processor for this model (usually arising from an inconsistency...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ts! bug ### Your current environment ```this is my code llm = LLM( model="/home/....../environment/internvl2_5/InternVL2_5-4B-MPO", trust_remote_code=True, # Required to load Phi-3.5-vision max_model_len=4096, # Otherwi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d Phi-3.5-vision max_model_len=4096, # Otherwise, it may not fit in smaller GPUs limit_mm_per_prompt={"image": 2}, # The maximum number to accept ) # Refer to the HuggingFace repo for the correct format to use prompt =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
