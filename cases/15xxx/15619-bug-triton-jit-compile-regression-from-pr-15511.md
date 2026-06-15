# vllm-project/vllm#15619: [Bug]: Triton JIT Compile Regression from PR 15511

| 字段 | 值 |
| --- | --- |
| Issue | [#15619](https://github.com/vllm-project/vllm/issues/15619) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Triton JIT Compile Regression from PR 15511

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug @wrmedford @LucasWilkinson There appears to be triton regression due to this PR #15511 I have tested torch 2.6 and 2.8 nightly and both throw this triton jit compile error of ```bash ERROR 03-27 12:41:06 [core.py:344] ptxas /tmp/tmp6qa78v4o.ptx, line 661; error : Modifier '.evict_last' cannot be combined with modifier '.cg' ``` ``` Name: triton Version: 3.2.0 Summary: A language and compiler for custom Deep Learning operations Home-page: https://github.com/triton-lang/triton/ Author: Philippe Tillet Author-email: phil@openai.com License: Location: /root/vm312/lib/python3.12/site-packages Requires: Required-by: torch ``` ```bash ERROR 03-27 12:41:06 [core.py:344] File "/root/vm312/lib/python3.12/site-packages/vllm/compilation/backends.py", line 608, in __call__ ERROR 03-27 12:41:06 [core.py:344] return self.compiled_graph_for_general_shape(*args) ERROR 03-27 12:41:06 [core.py:344] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-27 12:41:06 [core.py:344] File "/root/vm312/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 745, in _fn ERROR 03-27 12:41:06 [core.py:344] return fn(*args, **kwargs) ERROR 03-27 12:41:...

## 现有链接修复摘要

#15511 Use Cache Hinting for fused_moe kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Triton JIT Compile Regression from PR 15511 bug ### Your current environment ### 🐛 Describe the bug @wrmedford @LucasWilkinson There appears to be triton regression due to this PR #15511 I have tested torch 2.6 a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: triton jit compile error of ```bash ERROR 03-27 12:41:06 [core.py:344] ptxas /tmp/tmp6qa78v4o.ptx, line 661; error : Modifier '.evict_last' cannot be combined with modifier '.cg' ``` ``` Name: triton Version: 3.2.0 Summ...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Triton JIT Compile Regression from PR 15511 bug ### Your current environment ### 🐛 Describe the bug @wrmedford @LucasWilkinson There appears to be triton regression due to this PR #15511 I have tested torch 2.6 a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: call ERROR 03-27 12:41:06 [core.py:344] torch.ops.vllm.inplace_fused_experts.default(reinterpret_tensor(buf18, (s0, 7168), (7168, 1), 0), arg18_1, arg19_1, buf19, buf20, 'silu', False, False, True, 256, None, arg20_1, a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Triton JIT Compile Regression from PR 15511 bug ### Your current environment ### 🐛 Describe the bug @wrmedford @LucasWilkinson There appears to be triton regression due to this PR #15511 I have tested torch 2.6 a

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#15511](https://github.com/vllm-project/vllm/pull/15511) | mentioned | 0.45 | Use Cache Hinting for fused_moe kernel | @lucaswilkinson there appears to be triton regression due to this pr #15511 i have tested torch 2.6 and 2.8 nightly and both throw this triton jit compile error of ```bash error 0… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
