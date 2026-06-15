# vllm-project/vllm#4379: [Installation]: Question: Does pip package comes with PUNICA kernels? 

| 字段 | 值 |
| --- | --- |
| Issue | [#4379](https://github.com/vllm-project/vllm/issues/4379) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Question: Does pip package comes with PUNICA kernels? 

### Issue 正文摘录

### Your current environment ```text Irrelevant ``` ### How you are installing vllm ```sh pip install vllm==v0.4.0.post1 ``` My question is: Is my assumption that pip package comes with punica kernels, and is there any intention to change this in the future? I ran a couple of tests and it seems that at least `v0.4.0.post1` comes with punica kernels: ``` root@oandreeva-dt:/opt/tritonserver# python3 Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import vllm._punica_C as punica_kernels >>> exit() ``` I believe, this is intended: https://github.com/vllm-project/vllm/blob/15e7c675b0dc36109c7b591f856f102e96493a94/.github/workflows/scripts/build.sh#L16 P.S. please feel free to re-direct me to a dedicated Q&A resource for next time.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: Question: Does pip package comes with PUNICA kernels? installation ### Your current environment ```text Irrelevant ``` ### How you are installing vllm ```sh pip install vllm==v0.4.0.post1 ``` My quest
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ast `v0.4.0.post1` comes with punica kernels: ``` root@oandreeva-dt:/opt/tritonserver# python3 Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux Type "help", "copyright", "credits" or "license" for more...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: .0] on linux Type "help", "copyright", "credits" or "license" for more information. >>> import vllm._punica_C as punica_kernels >>> exit() ``` I believe, this is intended: https://github.com/vllm-project/vllm/blob/15e7c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: is there any intention to change this in the future? I ran a couple of tests and it seems that at least `v0.4.0.post1` comes with punica kernels: ``` root@oandreeva-dt:/opt/tritonserver# python3 Python 3.10.12 (main, No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
