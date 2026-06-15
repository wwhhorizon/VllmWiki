# vllm-project/vllm#13116: [Installation]: vllm requires the version of xformer==0.28.post3, while the latest version of xformers is 0.30, requiring torch=2.6.0, inconsistent with the 2.5.1 torch version requirements of vllm=0.7.2

| 字段 | 值 |
| --- | --- |
| Issue | [#13116](https://github.com/vllm-project/vllm/issues/13116) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: vllm requires the version of xformer==0.28.post3, while the latest version of xformers is 0.30, requiring torch=2.6.0, inconsistent with the 2.5.1 torch version requirements of vllm=0.7.2

### Issue 正文摘录

### Your current environment After I installed vllm=0.7.2, when I type python -m xformers.info, it throws error `undefined symbol: _ZN5torch8autograd12VariableInfoC1ERKN2at6TensorEb`. Details: `WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: PyTorch 2.6.0+cu124 with CUDA None (you have 2.5.1+cu121) Python 3.11.0 (you have 3.11.5) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) Memory-efficient attention, SwiGLU, sparse and more won't be available. Set XFORMERS_MORE_DETAILS=1 for more details` CUDA: 12.1 Torch: 2.5.1 GPU: V100 One more question: In the official documentation of vllm, it shows that the computing capability of GPU should be higher than 7.0, where V100 meets the requirement. While it seems that xformers need computing capability higher than 8.0. Can I use vllm under my GPU V100? Thanks so much. I look forward to the response. ### How you are installing vllm ```sh pip install vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: vllm requires the version of xformer==0.28.post3, while the latest version of xformers is 0.30, requiring torch=2.6.0, inconsistent with the 2.5.1 torch version requirements of vllm=0.7.2 installation;st...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ERKN2at6TensorEb`. Details: `WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: PyTorch 2.6.0+cu124 with CUDA None (you have 2.5.1+cu121) Python 3.11.0 (you have 3.11.5) Please reinstall...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ent with the 2.5.1 torch version requirements of vllm=0.7.2 installation;stale ### Your current environment After I installed vllm=0.7.2, when I type python -m xformers.info, it throws error `undefined symbol: _ZN5torch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: allation]: vllm requires the version of xformer==0.28.post3, while the latest version of xformers is 0.30, requiring torch=2.6.0, inconsistent with the 2.5.1 torch version requirements of vllm=0.7.2 installation;stale #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
