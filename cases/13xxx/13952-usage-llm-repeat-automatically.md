# vllm-project/vllm#13952: [Usage]: LLM repeat automatically

| 字段 | 值 |
| --- | --- |
| Issue | [#13952](https://github.com/vllm-project/vllm/issues/13952) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: LLM repeat automatically

### Issue 正文摘录

### Your current environment `#data generation from llama-3.1-8B from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.1-8B", dtype="float16", max_model_len=25000, enable_prefix_caching=False, enable_chunked_prefill=False) system_prompt = "你是一個專業的 AI 助理，專門針對台灣使用者優化回答。請確保回答用詞、語氣和語法符合台灣人的習慣與文化，讓使用者感覺自然。" #system_prompt = "You are an useful AI assistant." user_prompt = "請問台灣目前最受歡迎的飲料是什麼？" #user_prompt = "What is the most popular drink in Taiwan right now?" sampling_params = SamplingParams( temperature=0.5, # 調整隨機性 top_p=0.95, # 取樣範圍 max_tokens=256, # 限制回應長度 stop_token_ids=[" "] ) chat_prompt = f" \n{system_prompt}\n \n{user_prompt}\n " outputs = llm.generate([chat_prompt], sampling_params) print(outputs[0].outputs[0].text) ` 台灣最受歡迎的飲料是奶茶，下圖是台灣各地最受歡迎的奶茶品牌。 你是一個專業的 AI 助理，專門針對台灣使用者優化回答。請確保回答用詞、語氣和語法符合台灣人的習慣與文化，讓使用者感覺自然。 請問台灣目前最受歡迎的飲料是什麼？ 台灣最受歡迎的飲料是奶茶，下圖是台灣各地最受歡迎的奶茶品牌。 你是一個專業的 AI 助理，專門針對台灣使用者優化回答。請確保回答用詞、語氣和語法符合台灣人的習慣與文化，讓使用者感覺自然。 請問台灣目前最受歡迎的飲料是什麼？ 台灣最受歡迎的飲料是奶茶，下圖是台灣各地最受歡迎的奶茶品牌。 你是一個專業 為什麼輸出看起來好像重複執行了多次推理，但明明程式碼只執行了一次？ Why does the output appear to repeat the inference multiple times, when the code was only executed once? ### How would you like to use vllm I want to ru...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tically usage;stale ### Your current environment `#data generation from llama-3.1-8B from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.1-8B", dtype="float16", max_model_len=25000, enable_prefix_ca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: m import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.1-8B", dtype="float16", max_model_len=25000, enable_prefix_caching=False, enable_chunked_prefill=False) system_prompt = "你是一個專業的 AI 助理，專門針對台灣使用者優化回答。請確保回答...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: LLM repeat automatically usage;stale ### Your current environment `#data generation from llama-3.1-8B from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.1-8B", dtype="float16", max_model_l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Your current environment `#data generation from llama-3.1-8B from vllm import LLM, SamplingParams llm = LLM(model="meta-llama/Llama-3.1-8B", dtype="float16", max_model_len=25000, enable_prefix_caching=False, enable_chun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
