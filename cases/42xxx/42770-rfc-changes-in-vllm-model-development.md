# vllm-project/vllm#42770: [RFC]: Changes in vLLM Model Development

| 字段 | 值 |
| --- | --- |
| Issue | [#42770](https://github.com/vllm-project/vllm/issues/42770) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | activation;attention;cache;cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Changes in vLLM Model Development

### Issue 正文摘录

### Motivation. vLLM has long pursued the goal of building a unified, fast inference engine across diverse models and hardware. We remain committed to this goal, but we have come to believe that vLLM's current model implementation principles need to be revisited in order to improve both performance and development velocity. Two lessons stand out: * We were overly reluctant to modify model code directly for op fusion and kernel dispatching. Instead, we accumulated abstractions and compiler passes that ultimately made the code opaque and hard to optimize. * We pursued the unrealistic ideal of a single model definition that works well on every hardware. In practice, each hardware backend benefits from its own model implementation, since different hardware favors different fusion strategies. * AI coding agents have made manual op fusion and kernel writing much easier, and the agents work best with raw model code. To address these issues, we are making three fundamental changes to how vLLM implements and optimizes models: 1. Removing full-graph `torch.compile` requirement 2. Separation of model code across hardware backends 3. A clear model interface ## **1\. Removing full-graph `torch...

## 现有链接修复摘要

#42304 [Experimental] Breakable CUDA graph

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: spatching logic (for example, when different kernels must be launched on Hopper vs. Blackwell) possibly with some shared utility methods. For example, the code may look like: ```py def add_rms_norm_quant( hidden_states:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [RFC]: Changes in vLLM Model Development RFC ### Motivation. vLLM has long pursued the goal of building a unified, fast inference engine across diverse models and hardware. We remain committed to this goal, but we have...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Model Development RFC ### Motivation. vLLM has long pursued the goal of building a unified, fast inference engine across diverse models and hardware. We remain committed to this goal, but we have come to believe that vL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: overly reluctant to modify model code directly for op fusion and kernel dispatching. Instead, we accumulated abstractions and compiler passes that ultimately made the code opaque and hard to optimize. * We pursued the u...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: # pre-allreduce # Call the fused kernel here. residual, quantized_inputs = add_rms_norm_quant( hidden_states, residual, self.rms_norm.weights, self.rms_norm.eps, # act_quant_kwargs depends on the quantization scheme

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42304](https://github.com/vllm-project/vllm/pull/42304) | mentioned | 0.45 | [Experimental] Breakable CUDA graph | @zjy0516 implements pw cuda graph without relying on `torch.compile` #42304 * @woosukkwon implements the initial hardware separation for deepseek v4 & @tjtanaa will handle the amd… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
