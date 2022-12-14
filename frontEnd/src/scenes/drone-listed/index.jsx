import React from "react";
import DataTable from "../../components/DataTable";
import ContentHeader from "../../components/ContentHeader";
const columns = [
  { id: "name", label: "Model Name", minWidth: 170 },
  { id: "uin", label: "UIN", minWidth: 100 },
  {
    id: "service",
    label: "Time in Services",
    minWidth: 170,
  },
  {
    id: "maintenance",
    label: "Next Maintenance",
    minWidth: 170,
  },
  {
    id: "yop",
    label: "Year of Purchase",
    minWidth: 170,
  },
];

const rows = [
  {
    name: "QQ123",
    uin: 13213213213,
    service: "dd/mm/yyyy",
    maintenance: "dd/mm/yyyy",
    yop: "dd/mm/yyyy",
  },
  {
    name: "QQ123",
    uin: 2424214323,
    service: "dd/mm/yyyy",
    maintenance: "dd/mm/yyyy",
    yop: "dd/mm/yyyy",
  },
  {
    name: "QQ123",
    uin: 7563453267,
    service: "dd/mm/yyyy",
    maintenance: "dd/mm/yyyy",
    yop: "dd/mm/yyyy",
  },
];

export default function DronListed() {
  return (
    <div className="main">
      <ContentHeader pageTilte="drone listed" />
      <DataTable columns={columns} rows={rows} />
    </div>
  );
}
