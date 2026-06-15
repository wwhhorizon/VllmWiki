# vllm-project/vllm#7379: [Performance]: vllm inference in CPU instance has generation < 10 tokens / second

| 字段 | 值 |
| --- | --- |
| Issue | [#7379](https://github.com/vllm-project/vllm/issues/7379) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: vllm inference in CPU instance has generation < 10 tokens / second

### Issue 正文摘录

### Debug performance issue in CPU instance Hello! I'm trying to figure out the reason behind this performance, and would appreciate very much for the help here. - Instance: a CPU instance of Standard_E4ds_v4 (4 cores, 32 GB RAM, 150 GB disk) - LLM: llama3-8b This is a working code sample: ```python # vllm_config.yaml # SamplingParam: # temperature: 0.2 # top_p: 0.95 # max_tokens: 258 llm = LLM(model="meta-llama/Meta-Llama-3-8B", tensor_parallel_size=1) vllm_config = load_vllm_config(args.vllm_config) sampling_params = SamplingParams( temperature=vllm_config["SamplingParam"]["temperature"], top_p=vllm_config["SamplingParam"]["top_p"], max_tokens=vllm_config["SamplingParam"]["max_tokens"], ) example_json = {} prompt_list = build_prompt_list(dataset, example_json) responses = batch_llm_generation(llm, prompt_list, sampling_params) def build_prompt_list(ds: Dataset, examples: dict) -> List[str]: """Build a list of prompt strings to be fed to llama3 base model. Args: ds (Dataset): The full or partial of our example dataset. examples (dict): A dictionary of examples to build few shot prompts. Returns: prompt_list (List): A list of prompt strings. """ prompt_list = [] system_message = "...

## 现有链接修复摘要

#40795 [Core] Token-level DP load balancing for prefill-heavy workloads

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: trying to figure out the reason behind this performance, and would appreciate very much for the help here. - Instance: a CPU instance of Standard_E4ds_v4 (4 cores, 32 GB RAM, 150 GB disk) - LLM: llama3-8b This is a work...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: rsion__ as VLLM_VERSION PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: None ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (conda-forge gcc 14.1.0-0) 14.1.0 Cl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: PU instance of Standard_E4ds_v4 (4 cores, 32 GB RAM, 150 GB disk) - LLM: llama3-8b This is a working code sample: ```python # vllm_config.yaml # SamplingParam: # temperature: 0.2 # top_p: 0.95 # max_tokens: 258 llm = LL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Reg file data sampling: Not affected Vulnerability Retbl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ed_sequence.text) return generations ``` ### Report of performance regression The generation throughput varies, max is ~ 1024 tokens / 4 minute = ~ 4 tokens / second. ### Misc discussion on performance _No response_ ###...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40795](https://github.com/vllm-project/vllm/pull/40795) | mentioned | 0.6 | [Core] Token-level DP load balancing for prefill-heavy workloads | balancing, similar to sglang's --load-balance-method minimum_tokens ([sgl-project/sglang#7379](https://github.com/sgl-project/sglang/pull/7379)), but saw no improvement when teste… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
