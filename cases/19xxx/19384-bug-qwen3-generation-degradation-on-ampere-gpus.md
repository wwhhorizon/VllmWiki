# vllm-project/vllm#19384: [Bug]: Qwen3 generation degradation on ampere GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#19384](https://github.com/vllm-project/vllm/issues/19384) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 generation degradation on ampere GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3 generation massively degraded on A100 machines when set to larger batch size (generating un-usable results), while results with same configuration on H100 machines are fine. ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams import json model_path="Qwen3/Qwen3-32B" tokenizer = AutoTokenizer.from_pretrained(model_path) sampling_params = SamplingParams(temperature=0.6, top_p=0.95, max_tokens=4096) # same issue with temp=0 llm = LLM(model=model_path, tensor_parallel_size=8) path = "bon_think_score.jsonl" # see file linked (PPE correctness set with judge prompt) prompts = [] test_batch = 256 with open(path, "r") as f: for l in f: prompts.append(json.loads(l)['src']) if len(lines) == test_batch: break messages = [[{"role": "user", "content": prompt}] for prompt in prompts] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) outputs = llm.generate(text, sampling_params) # output degraded with len(text)>128 for this specific file ``` Run above code on A100 with test_batch > 128, the results are either repetitive or barely following the instructions (not o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: me configuration on H100 machines are fine. ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams import json model_path="Qwen3/Qwen3-32B" tokenizer = AutoTokenizer.from_pretrained(model_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Qwen3 generation degradation on ampere GPUs bug ### Your current environment ### 🐛 Describe the bug Qwen3 generation massively degraded on A100 machines when set to larger batch size (generating un-usable results...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 generation degradation on ampere GPUs bug ### Your current environment ### 🐛 Describe the bug Qwen3 generation massively degraded on A100 machines when set to larger batch size (generating un-usable results...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rontend_api;hardware_porting;model_support;sampling_logits cuda;sampling;triton build_error env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mpts] text = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) outputs = llm.generate(text, sampling_params) # output degraded with len(text)>128 for this specific file ``` Run above...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
