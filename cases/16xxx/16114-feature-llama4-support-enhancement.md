# vllm-project/vllm#16114: [Feature]: Llama4 Support Enhancement

| 字段 | 值 |
| --- | --- |
| Issue | [#16114](https://github.com/vllm-project/vllm/issues/16114) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cache;fp8;gemm;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Llama4 Support Enhancement

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We would like to further enhance the support for Llama4 Engine / Features - [ ] V0 enhancement and evaluation - [x] PP @zhewenl (https://github.com/vllm-project/vllm/issues/16231) - [ ] KV Cache Management enhancement for local attention @luccafong - [ ] FP8 + 16 Expert (Scout) - [ ] Int4 + 16 Expert (Scout) @liuzijing2014 - [x] TP4 Scout @sarckk (https://github.com/vllm-project/vllm/pull/16311) - [ ] Turn on temperature turning by default @luccafong https://github.com/vllm-project/vllm/pull/16216 - [x] Tool Parser @yeqcharlotte (https://github.com/vllm-project/vllm/issues/16214) (https://github.com/vllm-project/vllm/pull/16463) - [x] Relax image limit @yeqcharlotte (https://github.com/vllm-project/vllm/pull/16365) - [x] AMD + v0 @tjtanaa (https://github.com/vllm-project/vllm/pull/16198) Kernel / Perfs - [ ] Fused Experts - [ ] Fused Router - [ ] Integrate [Flex Attention Backend](https://github.com/vllm-project/vllm/pull/16078) for Local Chunked Attention @drisspg - [ ] FBGEMM support - [ ] MM Vision Encoder Optimization - [ ] EAGLE 3 - [ ] AMD Perf Enhancement @cthi @842974287 @xw285cornell - [x] H100 TP8 Scout tuning (https://github.com/v...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [ ] KV Cache Management enhancement for local attention @luccafong - [ ] FP8 + 16 Expert (Scout) - [ ] Int4 + 16 Expert (Scout) @liuzijing2014 - [x] TP4 Scout @sarckk (https://github.com/vllm-project/vllm/pull/16311) -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: che Management enhancement for local attention @luccafong - [ ] FP8 + 16 Expert (Scout) - [ ] Int4 + 16 Expert (Scout) @liuzijing2014 - [x] TP4 Scout @sarckk (https://github.com/vllm-project/vllm/pull/16311) - [ ] Turn...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Llama4 Support Enhancement feature request;stale ### 🚀 The feature, motivation and pitch We would like to further enhance the support for Llama4 Engine / Features - [ ] V0 enhancement and evaluation - [x] PP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Llama4 Support Enhancement feature request;stale ### 🚀 The feature, motivation and pitch We would like to further enhance the support for Llama4 Engine / Features - [ ] V0 enhancement and evaluation - [x] PP...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s - [ ] Fused Experts - [ ] Fused Router - [ ] Integrate [Flex Attention Backend](https://github.com/vllm-project/vllm/pull/16078) for Local Chunked Attention @drisspg - [ ] FBGEMM support - [ ] MM Vision Encoder Optimi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
