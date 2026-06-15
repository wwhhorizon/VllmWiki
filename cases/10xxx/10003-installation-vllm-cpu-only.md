# vllm-project/vllm#10003: [Installation]: vllm CPU only

| 字段 | 值 |
| --- | --- |
| Issue | [#10003](https://github.com/vllm-project/vllm/issues/10003) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm CPU only

### Issue 正文摘录

### Your current environment i am trying to install vllm CPU only on kaggle, using code bellow, i am not sure i am doing the right thing here, if not, please can someone give a step-by-step guide. after running this ``` from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) ``` i got this error ``` INFO 11-04 22:26:51 cpu_executor.py:207] # CPU blocks: 7281 ERROR 11-04 22:26:53 _custom_ops.py:63] Error in calling custom op reshape_and_cache: '_OpNamespace' '_C_cache_ops' object has no attribute 'reshape_and_cache' ERROR 11-04 22:26:53 _custom_ops.py:63] Possibly you have built or installed an obsolete version of vllm. ERROR 11-04 22:26:53 _custom_ops.py:63] Please try a clean build and install of vllm,or remove old built files such as vllm/*cpython*.so and build/ . ... ---> 15 outputs = llm.generate(prompts, sampling_params) ... AttributeError: '_OpNamespace' '_C_cache_ops' object has no attribute 'reshape_and_cache' ``` ### cur...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: vllm CPU only installation ### Your current environment i am trying to install vllm CPU only on kaggle, using code bellow, i am not sure i am doing the right thing here, if not, please can someone give a
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: will not be available. PyTorch version: 2.4.0+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) ``` i got this error ``` INFO 11-04 22:26:51 cpu_executor.py:207] # CPU...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `` i got this error ``` INFO 11-04 22:26:51 cpu_executor.py:207] # CPU blocks: 7281 ERROR 11-04 22:26:53 _custom_ops.py:63] Error in calling custom op reshape_and_cache: '_OpNamespace' '_C_cache_ops' object has no attri...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
