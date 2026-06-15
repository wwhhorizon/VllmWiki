# vllm-project/vllm#8361: [Bug]: internvl2 multi-prompt input with one image each get RuntimeError

| 字段 | 值 |
| --- | --- |
| Issue | [#8361](https://github.com/vllm-project/vllm/issues/8361) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: internvl2 multi-prompt input with one image each get RuntimeError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I init the mode with ``` python from vllm import LLM, SamplingParams load_dir=""OpenGVLab/InternVL2-8B"" llm = LLM( model=load_dir, trust_remote_code=True, max_num_seqs=5, max_model_len=8192, ) tokenizer = AutoTokenizer.from_pretrained(load_dir, trust_remote_code=True) stop_tokens = [" ", " ", " ", " "] stop_token_ids = [tokenizer.convert_tokens_to_ids(i) for i in stop_tokens] sampling_params = SamplingParams(temperature=0.2, max_tokens=8192, top_p=0.5, repetition_penalty=1.0, stop_token_ids=stop_token_ids) ``` I run the inference with ``` python llm.generate(prompt, sampling_params=sampling_params) ``` and the `prompt` is as below ``` json [{'multi_modal_data': {'image': }, 'prompt': ' user\n{prompt_text} \n assistant\n'}, {'multi_modal_data': {'image': }, 'prompt': ' user\n{prompt_text} \n assistant\n'}, {'multi_modal_data': {'image': }, 'prompt': ' user\n{prompt_text} \n assistant\n'}] ``` where the `{prompt_text}` is some text. And I meet the ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https:/...

## 现有链接修复摘要

#8375 [Bugfix] Fix InternVL2 inference with various num_patches

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t ### 🐛 Describe the bug I init the mode with ``` python from vllm import LLM, SamplingParams load_dir=""OpenGVLab/InternVL2-8B"" llm = LLM( model=load_dir, trust_remote_code=True, max_num_seqs=5, max_model_len=8192, )...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: internvl2 multi-prompt input with one image each get RuntimeError bug ### Your current environment ### 🐛 Describe the bug I init the mode with ``` python from vllm import LLM, SamplingParams load_dir=""OpenGVLab/I
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error env_dependency #8375 [Bugfix] Fix InternVL2 inference with various num_patches Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;hardware_porting;model_support;sampling_logits cuda...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#8375](https://github.com/vllm-project/vllm/pull/8375) | closes_keyword | 0.95 | [Bugfix] Fix InternVL2 inference with various num_patches | FIX #8361 (*link existing issues this PR will resolve*) FIX #8369 **TODO** - [x] Add test to cover these cases. **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FIL |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
