# vllm-project/vllm#31345: [Bug]: The ‘’draft_tensor_parallel_size‘’ parameter of the Eagel3 draft model does not take effect

| 字段 | 值 |
| --- | --- |
| Issue | [#31345](https://github.com/vllm-project/vllm/issues/31345) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The ‘’draft_tensor_parallel_size‘’ parameter of the Eagel3 draft model does not take effect

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug According to the official documentation, the parameter "draft_tensor_parallel_size": 1 is supposed to be applied to the Eagle3 model. However, based on actual debugging, it was found that the number of tensor parallelisms (tp) of the Eagle model is consistent with that of the target model. The setting of tp for the draft model did not take effect as expected. ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct" enforce_eager=True, model=model, tensor_parallel_size=4 , gpu_memory_utilization=0.9, speculative_config={ "method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "draft_tensor_parallel_size": 1, "num_speculative_tokens": 3 }, ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` Sorry, I can't provide photos, I debug in vllm/vllm/v1/worker/gpu_model_runner.py, breaking after `self.drafter.load_model(s...

## 现有链接修复摘要

#31705 [BugFix] Support setting tp=1 for the Eagle draft model to take effect | #31886 [Feature][Bugfix] Support draft model tp any of speculative decode

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: our current environment ### 🐛 Describe the bug According to the official documentation, the parameter "draft_tensor_parallel_size": 1 is supposed to be applied to the Eagle3 model. However, based on actual debugging, it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sed on actual debugging, it was found that the number of tensor parallelisms (tp) of the Eagle model is consistent with that of the target model. The setting of tp for the draft model did not take effect as expected. ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: The ‘’draft_tensor_parallel_size‘’ parameter of the Eagel3 draft model does not take effect bug ### Your current environment ### 🐛 Describe the bug According to the official documentation, the parameter "draft_te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: The ‘’draft_tensor_parallel_size‘’ parameter of the Eagel3 draft model does not take effect bug ### Your current environment ### 🐛 Describe the bug According to the official documentation, the parameter "draft_te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: hasattr(self.drafter, "model") and is_mixture_of_experts(self.drafter.model) and self.parallel_config.enable_eplb ``` The parameters are as follows： self.drafter.model.model.layers[0].self_attn.qkv_proj.tp_size = 4 self...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31705](https://github.com/vllm-project/vllm/pull/31705) | closes_keyword | 0.95 | [BugFix] Support setting tp=1 for the Eagle draft model to take effect | Fixes #31345 --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [x] The purpose of the PR, such as "Fix some issue (link existing iss |
| [#31886](https://github.com/vllm-project/vllm/pull/31886) | mentioned | 0.6 | [Feature][Bugfix] Support draft model tp any of speculative decode | r_parallel_group` to deal with the problem. Possibly related to issue #31345 ## Test Plan Test in server mode, print acceptance length to evaluate draft model accuracy with differ… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
