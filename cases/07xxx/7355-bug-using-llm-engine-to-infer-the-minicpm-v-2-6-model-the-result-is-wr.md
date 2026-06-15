# vllm-project/vllm#7355: [Bug]: Using LLM Engine to infer the MiniCPM-V-2_6 model, the result is wrong

| 字段 | 值 |
| --- | --- |
| Issue | [#7355](https://github.com/vllm-project/vllm/issues/7355) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Using LLM Engine to infer the MiniCPM-V-2_6 model, the result is wrong

### Issue 正文摘录

### Your current environment python 3.10 vllm 0.5.4 ### 🐛 Describe the bug There is no problem running with the official demo: ``` from transformers import AutoTokenizer from PIL import Image from vllm import LLM, SamplingParams,EngineArgs,LLMEngine MODEL_NAME = "/media/sofun/linux/model/MiniCPM-V-2_6" # Also available for previous models # MODEL_NAME = "openbmb/MiniCPM-Llama3-V-2_5" # MODEL_NAME = "HwwwH/MiniCPM-V-2" image = Image.open("/home/sofun/桌面/graph.png").convert("RGB") tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True) llm = LLM( model=MODEL_NAME, trust_remote_code=True, gpu_memory_utilization=1, max_model_len=2048 ) messages = [{ "role": "user", "content": # Number of images "( ./ )" + \ "\n这是一张什么图片?" }] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) # Single Inference inputs = { "prompt": prompt, "multi_modal_data": { "image": image # Multi images, the number of images should be equal to that of `( ./ )` # "image": [image, image] }, } # Batch Inference # inputs = [{ # "prompt": prompt, # "multi_modal_data": { # "image": image # }, # } for _ in 2] # 2.6 stop_tokens = [' ', ' '] stop_token_ids = [...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 0.5.4 ### 🐛 Describe the bug There is no problem running with the official demo: ``` from transformers import AutoTokenizer from PIL import Image from vllm import LLM, SamplingParams,EngineArgs,LLMEngine MODEL_NAME = "/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Using LLM Engine to infer the MiniCPM-V-2_6 model, the result is wrong bug ### Your current environment python 3.10 vllm 0.5.4 ### 🐛 Describe the bug There is no problem running with the official demo: ``` from t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rams = SamplingParams( stop_token_ids=stop_token_ids, use_beam_search=True, temperature=0, best_of=3, max_tokens=1024 ) outputs = llm.generate(inputs, sampling_params=sampling_params) print(outputs[0].outputs[0].text) `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: }] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True ) # Single Inference inputs = { "prompt": prompt, "multi_modal_data": { "image": image # Multi images, the number of images...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: better for streaming, so I hope to use LLMEngine. ``` async def process_requests(engine: LLMEngine, test_prompts: List[Tuple[str,str, SamplingParams]]): # 在test_prompts中加一个id communicator = ZMQCommunicator() print(RED+f...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
