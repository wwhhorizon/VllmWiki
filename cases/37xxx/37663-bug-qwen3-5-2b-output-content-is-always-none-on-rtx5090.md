# vllm-project/vllm#37663: [Bug]: Qwen3.5-2B output content is always None on RTX5090

| 字段 | 值 |
| --- | --- |
| Issue | [#37663](https://github.com/vllm-project/vllm/issues/37663) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-2B output content is always None on RTX5090

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After running vllm serve, I write a python script to call Qwen3.5-2B with openai sdk. I find that the content is always None. The script to start Qwen3.5-2B is ` vllm serve Qwen/Qwen3.5-2B --tensor-parallel-size 1 --max-model-len 8192 --gpu-memory-utilization 0.8 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-prefix-caching --enforce-eager` Python script: ``` from openai import OpenAI import time, json PROMPT_TEMPLATE = "Tell me the result. Just return final response not output other things. {text}" items = [ {"text": "Tell me who you are"}, {"text": "7+2"}, {"text": "8+2"}, {"text": "9+2"}, {"text": "11+2"}, {"text": "12+2"}, {"text": "34+2"}, ] MODEL = "Qwen/Qwen3.5-2B" client = OpenAI( base_url="http://localhost:8000/v1", api_key="dummy", # vLLM doesn't require a real key ) print(f"Starting generation for {len(items)} messages...") t0 = time.time() results = [] for item in items: response = client.chat.completions.create( model=MODEL, messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(text=item["text"])}], temperature=1.0, top_p=0.95, max_tokens=2048, ) print() print(respon...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3.5-2B output content is always None on RTX5090 bug ### Your current environment ### 🐛 Describe the bug After running vllm serve, I write a python script to call Qwen3.5-2B with openai sdk. I find that the co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: --enable-prefix-caching --enforce-eager` Python script: ``` from openai import OpenAI import time, json PROMPT_TEMPLATE = "Tell me the result. Just return final response not output other things. {text}" items = [ {"text...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3.5-2B output content is always None on RTX5090 bug ### Your current environment ### 🐛 Describe the bug After running vllm serve, I write a python script to call Qwen3.5-2B with openai sdk. I find that the co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pan multilingual support with fluent interaction in 100+ languages, high-precision OCR, advanced programming integrations, long-context window handling up to 256K tokens, real-time graph understanding, specialized scien...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
