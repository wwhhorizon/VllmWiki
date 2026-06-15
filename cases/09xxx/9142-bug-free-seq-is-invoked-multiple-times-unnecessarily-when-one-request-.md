# vllm-project/vllm#9142: [Bug]: free_seq is invoked multiple times unnecessarily when one request is finished. 

| 字段 | 值 |
| --- | --- |
| Issue | [#9142](https://github.com/vllm-project/vllm/issues/9142) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: free_seq is invoked multiple times unnecessarily when one request is finished. 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There are two invocations for free_seq() if a request has finished. One case: def _process_sequence_group_outputs(): if seq.is_finished(): # print(f"free_seq at line number: {inspect.currentframe().f_lineno}") for scheduler in self.scheduler: scheduler.free_seq(seq) The second case: def _process_model_outputs(): if finished_now: for scheduler in self.scheduler: scheduler.free_finished_seq_groups() In the second case, free_finished_seq_groups() --> _free_finished_seq_group() --> _free_finished_seqs() --> free_seq(). What problem can be caused: def free_seq(self, seq: Sequence) -> None: """Free a sequence from a block table.""" self.block_manager.free(seq) However, it is worthy mentioning that block_manager actually avoid the problem due to its implementation: def free(self, seq: Sequence) -> None: if seq.seq_id not in self.block_tables: # Already freed or haven't been scheduled yet. return However, it is clear that it is better to avoid such an unnecessary invocation. ``` Python Sample code to reproduce the problem''' from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, thi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vocation. ``` Python Sample code to reproduce the problem''' from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, this is", "The president of the United States is", "The capital of France is", "The...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: free_seq is invoked multiple times unnecessarily when one request is finished. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There are two invocations for free_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: }") ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: free_seq(self, seq: Sequence) -> None: """Free a sequence from a block table.""" self.block_manager.free(seq) However, it is worthy mentioning that block_manager actually avoid the problem due to its implementation: def...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: one request is finished. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There are two invocations for free_seq() if a request has finished. One case: def _process_seque...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
