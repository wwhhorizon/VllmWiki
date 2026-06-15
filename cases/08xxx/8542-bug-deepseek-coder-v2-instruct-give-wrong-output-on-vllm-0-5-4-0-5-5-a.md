# vllm-project/vllm#8542: [Bug]: deepseek_Coder_v2_Instruct give wrong output on vllm==0.5.4, 0.5.5, and 0.6.1.post2 (others not tried) with huggingface standard usage

| 字段 | 值 |
| --- | --- |
| Issue | [#8542](https://github.com/vllm-project/vllm/issues/8542) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseek_Coder_v2_Instruct give wrong output on vllm==0.5.4, 0.5.5, and 0.6.1.post2 (others not tried) with huggingface standard usage

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the same standard way as on huggingface for deepseek-Coder-v2-Instruct, I can only get weird Chinese characters as output. from transformers import AutoTokenizer from vllm import LLM, SamplingParams max_model_len, tp_size = 8192, 8 model_name = "deepseek-ai/DeepSeek-Coder-V2-Instruct" tokenizer = AutoTokenizer.from_pretrained(model_name) llm = LLM(model=model_name, tensor_parallel_size=tp_size, max_model_len=max_model_len, trust_remote_code=True, enforce_eager=True) sampling_params = SamplingParams(temperature=0.3, max_tokens=256, stop_token_ids=[tokenizer.eos_token_id]) messages_list = [ [{"role": "user", "content": "Who are you?"}], [{"role": "user", "content": "write a quick sort algorithm in python."}], [{"role": "user", "content": "Write a piece of quicksort code in C++."}], ] prompt_token_ids = [tokenizer.apply_chat_template(messages, add_generation_prompt=True) for messages in messages_list] outputs = llm.generate(prompt_token_ids=prompt_token_ids, sampling_params=sampling_params) generated_text = [output.outputs[0].text for output in outputs] print(generated_text) Generated_t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ct, I can only get weird Chinese characters as output. from transformers import AutoTokenizer from vllm import LLM, SamplingParams max_model_len, tp_size = 8192, 8 model_name = "deepseek-ai/DeepSeek-Coder-V2-Instruct" t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e5) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng output on vllm==0.5.4, 0.5.5, and 0.6.1.post2 (others not tried) with huggingface standard usage bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When using the same s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ild;distributed_parallel;frontend_api;model_support;sampling_logits cuda;triton build_error;mismatch env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: allel;frontend_api;model_support;sampling_logits cuda;triton build_error;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
