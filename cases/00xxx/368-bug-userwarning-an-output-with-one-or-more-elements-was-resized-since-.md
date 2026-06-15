# vllm-project/vllm#368: [bug]：UserWarning: An output with one or more elements was resized since it had shape [10, 4096], which does not match the required output shape [16, 4096]. This behavior is deprecated, and in a future PyTorch release outputs will not be resized unless they have zero elements. You can explicitly reuse an out tensor t by resizing it, inplace, to zero elements with t.resize_(0). (Triggered internally at ../aten/src/ATen/native/Resize.cpp:26.) (Worker pid=15829)   torch.matmul(input_parallel, self.weight_t, out=output_buffer)

| 字段 | 值 |
| --- | --- |
| Issue | [#368](https://github.com/vllm-project/vllm/issues/368) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [bug]：UserWarning: An output with one or more elements was resized since it had shape [10, 4096], which does not match the required output shape [16, 4096]. This behavior is deprecated, and in a future PyTorch release outputs will not be resized unless they have zero elements. You can explicitly reuse an out tensor t by resizing it, inplace, to zero elements with t.resize_(0). (Triggered internally at ../aten/src/ATen/native/Resize.cpp:26.) (Worker pid=15829)   torch.matmul(input_parallel, self.weight_t, out=output_buffer)

### Issue 正文摘录

- run script： ``` python3 benchmark_latency.py --model=llama-7b \ --tensor-parallel-size 2 \ --batch-size=2 \ --input-len=5 \ --output-len=5 \ --num-iters=1 ``` - run results： (Worker pid=15829) /usr/local/lib/python3.8/dist-packages/vllm/model_executor/parallel_utils/tensor_parallel/layers.py:438: UserWarning: An output with one or more elements was resized since it had shape [10, 4096], which does not match the required output shape [16, 4096]. This behavior is deprecated, and in a future PyTorch release outputs will not be resized unless they have zero elements. You can explicitly reuse an out tensor t by resizing it, inplace, to zero elements with t.resize_(0). (Triggered internally at ../aten/src/ATen/native/Resize.cpp:26.) (Worker pid=15829) torch.matmul(input_parallel, self.weight_t, out=output_buffer)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t_t, out=output_buffer) - run script： ``` python3 benchmark_latency.py --model=llama-7b \ --tensor-parallel-size 2 \ --batch-size=2 \ --input-len=5 \ --output-len=5 \ --num-iters=1 ``` - run results： (Worker pid=15829)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ut_parallel, self.weight_t, out=output_buffer) - run script： ``` python3 benchmark_latency.py --model=llama-7b \ --tensor-parallel-size 2 \ --batch-size=2 \ --input-len=5 \ --output-len=5 \ --num-iters=1 ``` - run resul...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: outputs will not be resized unless they have zero elements. You can explicitly reuse an out tensor t by resizing it, inplace, to zero elements with t.resize_(0). (Triggered internally at ../aten/src/ATen/native/Resize.c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
