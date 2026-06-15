# vllm-project/vllm#23226: [Bug][Dynamo] Support construction of TensorSchema

| 字段 | 值 |
| --- | --- |
| Issue | [#23226](https://github.com/vllm-project/vllm/issues/23226) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Dynamo] Support construction of TensorSchema

### Issue 正文摘录

### Your current environment TBD ### 🐛 Describe the bug What: Add support for TensorSchema in user-defined objects for compatibility with Dynamo's tracing system. Why: Observed graph breaks similar to prior issue with TypedDict - https://github.com/pytorch/pytorch/issues/132629 ``` def test_tensor_schema_llava_pixel_inputs(self): class LlavaImagePixelInputs(TensorSchema): type: Literal["pixel_values"] = "pixel_values" pixel_values: Annotated[ torch.Tensor, TensorShape("bn", 3, "h", "w") ] def fn(x, y): obj = LlavaImagePixelInputs(pixel_values=y) return x * obj.pixel_values.sum() x, y = torch.randn(4), torch.randn(2, 3, 8, 8) ref = fn(x, y) opt_fn = torch.compile(fn, backend="eager", fullgraph=True) res = opt_fn(x, y) self.assertEqual(ref, res) ``` ``` ERROR: test_tensor_schema_llava_pixel_inputs (caffe2.test.dynamo.test_repros.ReproTests) ---------------------------------------------------------------------- Traceback (most recent call last): File "/data/users/benjibeck/fbsource/buck-out/v2/gen/fbcode/95f6e7be6bb24603/caffe2/test/dynamo/__test_repros__/test_repros#link-tree/caffe2/test/dynamo/test_repros.py", line 6544, in test_tensor_schema_llava_pixel_inputs res = opt_fn(x, y) F...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: TensorSchema in user-defined objects for compatibility with Dynamo's tracing system. Why: Observed graph breaks similar to prior issue with TypedDict - https://github.com/pytorch/pytorch/issues/132629 ``` def test_tenso...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ypedDict - https://github.com/pytorch/pytorch/issues/132629 ``` def test_tensor_schema_llava_pixel_inputs(self): class LlavaImagePixelInputs(TensorSchema): type: Literal["pixel_values"] = "pixel_values" pixel_values: An...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n(2, 3, 8, 8) ref = fn(x, y) opt_fn = torch.compile(fn, backend="eager", fullgraph=True) res = opt_fn(x, y) self.assertEqual(ref, res) ``` ``` ERROR: test_tensor_schema_llava_pixel_inputs (caffe2.test.dynamo.test_repros...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
