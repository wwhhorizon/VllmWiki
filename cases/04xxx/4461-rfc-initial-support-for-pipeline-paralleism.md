# vllm-project/vllm#4461: [RFC]: Initial support for Pipeline Paralleism

| 字段 | 值 |
| --- | --- |
| Issue | [#4461](https://github.com/vllm-project/vllm/issues/4461) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Initial support for Pipeline Paralleism

### Issue 正文摘录

### Motivation. This RFC describes the initial approach for supporting pipeline parallelism as part of vLLM. Pipeline parallelism is a technique that allows splitting up model layers across multiple devices, i.e. a 12 layer model may be partitioned across 4 devices, each taking care of 3 layers. As each device finishes the execution of its portion of layers, it sends its finished data to the next device allowing it to then move onto the next microbatch in a _pipelined_ fashion, hence the name. This is shown in the below image: ![ppworkers drawio](https://github.com/vllm-project/vllm/assets/37849411/7c3e387e-d430-4e53-b49c-a916a5efe652) Here, the input stage handles embedding (E) completes the first 3 layers and sends the result (S) to the next worker where it is received (R). The middle two workers execute their work after a recv and then send. The last worker recvs the output from the previous layer and then computes the relevant output (logits). Compared to tensor parallelism, this technique can have lower communication overhead. However tensor parallelism may allow increased batching allowing lower latency for a batch. These techniques are not exclusive however and can be combi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: there are 4 streams, each denoted by a different colour. We can imagine requests in each of these streams as being data dependent. Within one step (within which requests move from the first stage to the last stage, top...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: parallelism between nodes where communication is high) This PR will be important for very large models that require multiple boxes, as well as machines that have high communication overhead (no NVLink for example). ###...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ch virtual engine currently consists of its own scheduler (And therefore block manager) as well as a corresponding cache engine. This allows completely separate scheduling without interference. New requests can be added...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [RFC]: Initial support for Pipeline Paralleism RFC ### Motivation. This RFC describes the initial approach for supporting pipeline parallelism as part of vLLM. Pipeline parallelism is a technique that allows splitting u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: t of vLLM. Pipeline parallelism is a technique that allows splitting up model layers across multiple devices, i.e. a 12 layer model may be partitioned across 4 devices, each taking care of 3 layers. As each device finis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
