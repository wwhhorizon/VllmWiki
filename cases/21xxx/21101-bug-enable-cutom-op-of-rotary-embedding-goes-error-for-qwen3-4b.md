# vllm-project/vllm#21101: [Bug]: Enable cutom_op of rotary_embedding goes error for Qwen3-4B

| 字段 | 值 |
| --- | --- |
| Issue | [#21101](https://github.com/vllm-project/vllm/issues/21101) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Enable cutom_op of rotary_embedding goes error for Qwen3-4B

### Issue 正文摘录

### Your current environment torch version 2.7.1 vllm version 0.9.2rc2.dev304+g28a6d5423.cu124 compile myself depends on newset mast. ### 🐛 Describe the bug I modify vllm/config.py to enable rotary_embedding op to enable custom_op. modify: --- a/vllm/config.py +++ b/vllm/config.py @@ -4624,6 +4624,7 @@ class VllmConfig: not self.model_config.enforce_eager: # By default, V1 uses piecewise CUDA graphs. If full_cuda_graph # is set to True, full CUDA graphs will be used. + self.compilation_config.custom_ops=["none","+rotary_embedding”] run for Qwen3-4B for v1 mode torch.compile. return error as follows: ERROR 07-17 15:36:30 [core.py:592] File "/root/.virtualenvs/torch-env/lib/python3.10/site-packages/torch/fx/graph.py", line 1172, in erase_node ERROR 07-17 15:36:30 [core.py:592] raise RuntimeError( ERROR 07-17 15:36:30 [core.py:592] torch._inductor.exc.InductorError: RuntimeError: Tried to erase Node getitem_4 but it still had 1 users in the graph: {view_4: None}! ERROR 07-17 15:36:30 [core.py:592] ERROR 07-17 15:36:30 [core.py:592] Set TORCHDYNAMO_VERBOSE=1 for the internal stack trace (please do this especially if you're reporting a bug to PyTorch). For even more developer context,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ]: Enable cutom_op of rotary_embedding goes error for Qwen3-4B bug;torch.compile ### Your current environment torch version 2.7.1 vllm version 0.9.2rc2.dev304+g28a6d5423.cu124 compile myself depends on newset mast. ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Enable cutom_op of rotary_embedding goes error for Qwen3-4B bug;torch.compile ### Your current environment torch version 2.7.1 vllm version 0.9.2rc2.dev304+g28a6d5423.cu124 compile myself depends on newset mast....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model_config.enforce_eager: # By default, V1 uses piecewise CUDA graphs. If full_cuda_graph # is set to True, full CUDA graphs will be used. + self.compilation_config.custom_ops=["none","+rotary_embedding”] run for Qwen...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda;operator build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
