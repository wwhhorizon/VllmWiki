# vllm-project/vllm#15846: [Usage]: Qwen2.5VL inference speed is unusually slow, something wrong within my usage?

| 字段 | 值 |
| --- | --- |
| Issue | [#15846](https://github.com/vllm-project/vllm/issues/15846) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen2.5VL inference speed is unusually slow, something wrong within my usage?

### Issue 正文摘录

Qwen2.5VL 32B inference speed is unusually slow, with 2x Ascend 910 cards (TP=2), achieving only about 8~9 tokens/s. I'd like to ask what the normal speed would be approximately? ```python MODEL_PATH='Qwen2.5-VL-32B-Instruct' llm = LLM( model=MODEL_PATH, max_model_len=16384, max_num_seqs=1, limit_mm_per_prompt={"image": 2}, tensor_parallel_size=2, distributed_executor_backend="mp", ) sampling_params = SamplingParams( max_tokens=512 ) ``` ### current environment driver version.info ```text 1 Version=24.1.rc3 2 ascendhal_version=7.35.23 3 aicpu_version=1.0 4 tdt_version=1.0 5 log_version=1.0 6 prof_version=2.0 7 dvppkernels_version=1.1 8 tsfw_version=1.0 9 Innerversion=V100R001C19SPC001B124 10 compatible_version=[V100R001C13],[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19] 11 compatible_version_fw=[7.0.0,7.5.99] 12 package_version=24.1.rc3 ``` ascend-toolkit version.info ``` 1 # version: 1.0 2 runtime_running_version=[7.6.0.1.220:8.0.0] 3 compiler_running_version=[7.6.0.1.220:8.0.0] 4 hccl_running_version=[7.6.0.1.220:8.0.0] 5 opp_running_version=[7.6.0.1.220:8.0.0] 6 toolkit_running_version=[7.6.0.1.220:8.0.0] 7 aoe_running_version=[7.6.0.1.220:8.0.0] 8 ncs_running_version=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: amplingParams( max_tokens=512 ) ``` ### current environment driver version.info ```text 1 Version=24.1.rc3 2 ascendhal_version=7.35.23 3 aicpu_version=1.0 4 tdt_version=1.0 5 log_version=1.0 6 prof_version=2.0 7 dvppker...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen2.5VL inference speed is unusually slow, something wrong within my usage? usage Qwen2.5VL 32B inference speed is unusually slow, with 2x Ascend 910 cards (TP=2), achieving only about 8~9 tokens/s. I'd like...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rompt={"image": 2}, tensor_parallel_size=2, distributed_executor_backend="mp", ) sampling_params = SamplingParams( max_tokens=512 ) ``` ### current environment driver version.info ```text 1 Version=24.1.rc3 2 ascendhal_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 2 Ascend-cann-atb Version : 8.0.0.B100 3 Platform : aarch64 4 branch : br_release_cann_8.0.0_20250521 5 commit id : af0ec2e868267322b4fb7949da3ae7af769d9644 ``` ascend_tool_box_install.info ``` 1 version=6.0.RC1 2 arch=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
