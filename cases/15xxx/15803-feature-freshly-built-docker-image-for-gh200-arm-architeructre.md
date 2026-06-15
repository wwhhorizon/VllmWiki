# vllm-project/vllm#15803: [Feature]: Freshly built docker image for GH200/ARM architeructre

| 字段 | 值 |
| --- | --- |
| Issue | [#15803](https://github.com/vllm-project/vllm/issues/15803) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Freshly built docker image for GH200/ARM architeructre

### Issue 正文摘录

I really want to use Gemma 3 with vLLM, as it has shown good results on my local AMD64 machines. However, I lack an ARM machine to build a vLLM container for GH200 machines used on the Jupiter Jülich HPC. I would be very grateful if someone could build a container with the latest vLLM for GH200. I have found several older vLLM for GH200 containers that work with Gemma 2 perfectly well but have problems with Gemma 3, which were only recently solved. Thanks, Toms

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Freshly built docker image for GH200/ARM architeructre feature request;stale I really want to use Gemma 3 with vLLM, as it has shown good results on my local AMD64 machines. However, I lack an ARM machine to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Feature]: Freshly built docker image for GH200/ARM architeructre feature request;stale I really want to use Gemma 3 with vLLM, as it has shown good results on my local AMD64 machines. However, I lack an ARM machine to b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Freshly built docker image for GH200/ARM architeructre feature request;stale I really want to use Gemma 3 with vLLM, as it has shown good results on my local AMD64 machines. However, I lack an ARM machine to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e for GH200/ARM architeructre feature request;stale I really want to use Gemma 3 with vLLM, as it has shown good results on my local AMD64 machines. However, I lack an ARM machine to build a vLLM container for GH200 mac...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e for GH200/ARM architeructre feature request;stale I really want to use Gemma 3 with vLLM, as it has shown good results on my local AMD64 machines. However, I lack an ARM machine to build a vLLM container for GH200 mac...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
