# vllm-project/vllm#18902: [Bug]: The frequency penalty does not work when spec decoding is enabled in V1, with no warning or error

| 字段 | 值 |
| --- | --- |
| Issue | [#18902](https://github.com/vllm-project/vllm/issues/18902) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The frequency penalty does not work when spec decoding is enabled in V1, with no warning or error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello team, Thank you very much for your work! I have a problem with applying frequency penalties when spec decoding is enabled: ```python from vllm.entrypoints.llm import LLM, SamplingParams if __name__ == "__main__": MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct" SPEC_MODEL = "yuhuili/EAGLE-LLaMA3.1-Instruct-8B" llm = LLM( model=MODEL_NAME, max_model_len=1024, speculative_config={ "model": SPEC_MODEL, "num_speculative_tokens": 3, "method": "eagle", }, tensor_parallel_size=2, seed=0, ) prompt = "Repeat the word 'hello' multuple times: hello" for penalty in [-2.0, 2.0]: sampling_params = SamplingParams( temperature=0, max_tokens=8, frequency_penalty=penalty, ) outputs = llm.generate( prompts=prompt, use_tqdm=True, sampling_params=sampling_params, ) print(outputs[0].outputs[0].text) ``` As the result I get: ``` Adding requests: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 1606.40it/s] Processed prompts: 100%|██████████████████████████████████████████████████████████████████████████████████...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ties when spec decoding is enabled: ```python from vllm.entrypoints.llm import LLM, SamplingParams if __name__ == "__main__": MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct" SPEC_MODEL = "yuhuili/EAGLE-LLaMA3.1-Instr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: if I turn off spec decoding, it works well, and the second time I get a smaller number of words: 'hello'. As I understand, the main reason is the lack of the [logic](https://github.com/vllm-project/vllm/blob/v0.9.0/vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: trypoints.llm import LLM, SamplingParams if __name__ == "__main__": MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct" SPEC_MODEL = "yuhuili/EAGLE-LLaMA3.1-Instruct-8B" llm = LLM( model=MODEL_NAME, max_model_len=1024, s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t work when spec decoding is enabled in V1, with no warning or error bug;stale ### Your current environment ### 🐛 Describe the bug Hello team, Thank you very much for your work! I have a problem with applying frequency...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
