# vllm-project/vllm#14761: [Bug]: deepseek_r1_reasoning_parser.py      except      reasoning_content = self.reasoning_regex.findall(model_output)[0] IndexError: list index out of range

| 字段 | 值 |
| --- | --- |
| Issue | [#14761](https://github.com/vllm-project/vllm/issues/14761) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: deepseek_r1_reasoning_parser.py      except      reasoning_content = self.reasoning_regex.findall(model_output)[0] IndexError: list index out of range

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used vllm 0.7.3 V1 version model is deepseek distill 14B , use llmcompressor.transformers Quantization to FP8 when muilt request to the vllm server ![Image](https://github.com/user-attachments/assets/57b46ad5-f9f2-4520-b90f-c33a0d18aa49) sometimes server raise exception : await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/_exception_handler.py", line 53, in wrapped_app raise exc File "/usr/local/lib/python3.10/dist-packages/starlette/_exception_handler.py", line 42, in wrapped_app await app(scope, receive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 735, in app await route.handle(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 288, in handle await self.app(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 76, in app await wrap_app_handling_exceptions(app, request)(scope, receive, sen...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rsion model is deepseek distill 14B , use llmcompressor.transformers Quantization to FP8 when muilt request to the vllm server ![Image](https://github.com/user-attachments/assets/57b46ad5-f9f2-4520-b90f-c33a0d18aa49) so...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ur current environment ### 🐛 Describe the bug I used vllm 0.7.3 V1 version model is deepseek distill 14B , use llmcompressor.transformers Quantization to FP8 when muilt request to the vllm server ![Image](https://github...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nge ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ser.py except reasoning_content = self.reasoning_regex.findall(model_output)[0] IndexError: list index out of range bug ### Your current environment ### 🐛 Describe the bug I used vllm 0.7.3 V1 version model is deepseek...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
