# vllm-project/vllm#3795: [Bug]: FastAPI Swagger /docs does not working correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#3795](https://github.com/vllm-project/vllm/issues/3795) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FastAPI Swagger /docs does not working correctly

### Issue 正文摘录

### Your current environment The latest vLLM docker: vllm/vllm-openai:v0.4.0 Issue seems to exist as far back as 0.2.7. ### 🐛 Describe the bug Visiting **http://localhost:8080/docs** when running the server offline shows a blank page however loads with the proper title for the page. I haven't yet attempted this with an online / non-firewalled running instance of vLLM. Inspecting the page with developer tools shows some html, however there are errors in downloading .js files from a cdn so I suspect that is the problem. Is there a way to enable support for the Swagger documentation offline? Since I'm unable to test, http://localhost:8080/docs properly functioning with online instances?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: not working correctly bug ### Your current environment The latest vLLM docker: vllm/vllm-openai:v0.4.0 Issue seems to exist as far back as 0.2.7. ### 🐛 Describe the bug Visiting **http://localhost:8080/docs** when runni...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /docs does not working correctly bug ### Your current environment The latest vLLM docker: vllm/vllm-openai:v0.4.0 Issue seems to exist as far back as 0.2.7. ### 🐛 Describe the bug Visiting **http://localhost:8080/docs**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
